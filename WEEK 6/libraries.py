import requests
import os
import hashlib
from urllib.parse import urlparse

def get_safe_filename(url):
    """Extract filename from URL or generate one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        filename = "downloaded_image.jpg"
    return filename

def file_hash(filepath):
    """Generate a hash of a file to detect duplicates."""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs separated by spaces
    urls = input("Please enter one or more image URLs (separated by spaces): ").split()

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Keep a set of hashes to prevent duplicates
    existing_hashes = set()
    for file in os.listdir("Fetched_Images"):
        filepath = os.path.join("Fetched_Images", file)
        if os.path.isfile(filepath):
            existing_hashes.add(file_hash(filepath))

    for url in urls:
        try:
            # Fetch the image with headers
            response = requests.get(url, timeout=10, headers={'User-Agent': 'Ubuntu Image Fetcher'})
            response.raise_for_status()

            # Check for content type to ensure it's an image
            content_type = response.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                print(f"✗ Skipped: {url} (Not an image: {content_type})")
                continue

            # Prepare filename and path
            filename = get_safe_filename(url)
            filepath = os.path.join("Fetched_Images", filename)

            # Check duplicate by comparing content hash
            new_hash = hashlib.md5(response.content).hexdigest()
            if new_hash in existing_hashes:
                print(f"✗ Duplicate skipped: {filename}")
                continue

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            existing_hashes.add(new_hash)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
