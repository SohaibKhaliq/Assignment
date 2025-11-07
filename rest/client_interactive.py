"""
REST Interactive Client - Book Management System
================================================
This interactive client provides a user-friendly menu system for managing
books through the REST API.

Features:
- Interactive menu for CRUD operations
- Input validation and error handling
- Formatted display of books
- Multiple operations in one session

Usage:
1. Start the REST API server: python app.py
2. Run this interactive client: python client_interactive.py
3. Follow the menu prompts
"""

import requests
import sys
import json

# API Base URL
BASE_URL = 'http://127.0.0.1:5000'

def print_header():
    """Print the application header."""
    print("=" * 70)
    print("REST API INTERACTIVE CLIENT - Book Management System")
    print("=" * 70)
    print(f"API Server: {BASE_URL}")
    print("=" * 70)


def print_menu():
    """Print the main menu."""
    print("\n" + "-" * 70)
    print("BOOK MANAGEMENT MENU")
    print("-" * 70)
    print("  1. View all books (GET /books)")
    print("  2. View a specific book (GET /books/<id>)")
    print("  3. Add a new book (POST /books)")
    print("  4. Update a book (PUT /books/<id>)")
    print("  5. Delete a book (DELETE /books/<id>)")
    print("  6. Exit")
    print("-" * 70)


def display_books(books_data):
    """
    Display books in a formatted table.
    
    Args:
        books_data (dict): Dictionary of books
    """
    if not books_data:
        print("  No books found.")
        return
    
    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Price':>10}")
    print("-" * 70)
    
    for book_id, book in books_data.items():
        print(f"{book_id:<5} {book['title']:<30} {book['author']:<20} ${book['price']:>9.2f}")
    
    print("=" * 70)


def get_all_books():
    """View all books in the system."""
    try:
        print("\n[GET] Fetching all books from /books...")
        response = requests.get(f'{BASE_URL}/books')
        
        if response.status_code == 200:
            books = response.json()
            print(f"[SUCCESS] Retrieved {len(books)} book(s)")
            display_books(books)
        else:
            print(f"[ERROR] Status {response.status_code}: {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to the API server. Is it running?")
    except Exception as e:
        print(f"[ERROR] {e}")


def get_book_by_id():
    """View a specific book by ID."""
    try:
        book_id = input("\nEnter book ID: ").strip()
        
        if not book_id.isdigit():
            print("[ERROR] Book ID must be a number.")
            return
        
        print(f"\n[GET] Fetching book from /books/{book_id}...")
        response = requests.get(f'{BASE_URL}/books/{book_id}')
        
        if response.status_code == 200:
            book_data = response.json()
            print("[SUCCESS] Book found!")
            display_books(book_data)
        elif response.status_code == 404:
            print(f"[ERROR] Book with ID {book_id} not found.")
        else:
            print(f"[ERROR] Status {response.status_code}: {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to the API server.")
    except Exception as e:
        print(f"[ERROR] {e}")


def add_book():
    """Add a new book to the system."""
    try:
        print("\n" + "-" * 70)
        print("ADD NEW BOOK")
        print("-" * 70)
        
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        price_str = input("Enter price: ").strip()
        
        # Validation
        if not title or not author:
            print("[ERROR] Title and author cannot be empty.")
            return
        
        try:
            price = float(price_str)
            if price < 0:
                print("[ERROR] Price cannot be negative.")
                return
        except ValueError:
            print("[ERROR] Invalid price format.")
            return
        
        # Prepare request data
        book_data = {
            "title": title,
            "author": author,
            "price": price
        }
        
        print(f"\n[POST] Creating new book at /books...")
        print(f"Data: {json.dumps(book_data, indent=2)}")
        
        response = requests.post(f'{BASE_URL}/books', json=book_data)
        
        if response.status_code == 201:
            result = response.json()
            print(f"[SUCCESS] Book added successfully!")
            print(f"  New Book ID: {result['id']}")
            print(f"  Message: {result['message']}")
        else:
            print(f"[ERROR] Status {response.status_code}: {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to the API server.")
    except Exception as e:
        print(f"[ERROR] {e}")


def update_book():
    """Update an existing book."""
    try:
        book_id = input("\nEnter book ID to update: ").strip()
        
        if not book_id.isdigit():
            print("[ERROR] Book ID must be a number.")
            return
        
        print("\nEnter new values (press Enter to skip):")
        title = input("New title: ").strip()
        author = input("New author: ").strip()
        price_str = input("New price: ").strip()
        
        # Build update data with only provided fields
        update_data = {}
        if title:
            update_data['title'] = title
        if author:
            update_data['author'] = author
        if price_str:
            try:
                price = float(price_str)
                if price < 0:
                    print("[ERROR] Price cannot be negative.")
                    return
                update_data['price'] = price
            except ValueError:
                print("[ERROR] Invalid price format.")
                return
        
        if not update_data:
            print("[WARNING] No fields to update.")
            return
        
        print(f"\n[PUT] Updating book at /books/{book_id}...")
        print(f"Data: {json.dumps(update_data, indent=2)}")
        
        response = requests.put(f'{BASE_URL}/books/{book_id}', json=update_data)
        
        if response.status_code == 200:
            result = response.json()
            print(f"[SUCCESS] {result['message']} (ID: {result['id']})")
        elif response.status_code == 404:
            print(f"[ERROR] Book with ID {book_id} not found.")
        else:
            print(f"[ERROR] Status {response.status_code}: {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to the API server.")
    except Exception as e:
        print(f"[ERROR] {e}")


def delete_book():
    """Delete a book from the system."""
    try:
        book_id = input("\nEnter book ID to delete: ").strip()
        
        if not book_id.isdigit():
            print("[ERROR] Book ID must be a number.")
            return
        
        # Confirmation
        confirm = input(f"Are you sure you want to delete book ID {book_id}? (yes/no): ").strip().lower()
        
        if confirm != 'yes':
            print("[CANCELLED] Delete operation cancelled.")
            return
        
        print(f"\n[DELETE] Deleting book at /books/{book_id}...")
        response = requests.delete(f'{BASE_URL}/books/{book_id}')
        
        if response.status_code == 200:
            result = response.json()
            print(f"[SUCCESS] {result['message']} (ID: {result['id']})")
        elif response.status_code == 404:
            print(f"[ERROR] Book with ID {book_id} not found.")
        else:
            print(f"[ERROR] Status {response.status_code}: {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to the API server.")
    except Exception as e:
        print(f"[ERROR] {e}")


def main():
    """Main application loop."""
    print_header()
    
    # Test connection
    try:
        print("\n[INFO] Testing connection to API server...")
        response = requests.get(f'{BASE_URL}/books', timeout=2)
        print("[INFO] ✓ Connection successful!")
    except requests.exceptions.ConnectionError:
        print("[ERROR] ✗ Cannot connect to API server!")
        print("Please make sure the server is running: python app.py")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    
    operation_count = 0
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            get_all_books()
            operation_count += 1
        elif choice == '2':
            get_book_by_id()
            operation_count += 1
        elif choice == '3':
            add_book()
            operation_count += 1
        elif choice == '4':
            update_book()
            operation_count += 1
        elif choice == '5':
            delete_book()
            operation_count += 1
        elif choice == '6':
            print("\n[EXIT] Exiting application...")
            break
        else:
            print("[WARNING] Invalid choice. Please enter 1-6.")
    
    print("\n" + "=" * 70)
    print(f"[SUMMARY] Total operations performed: {operation_count}")
    print("Thank you for using the Book Management System!")
    print("=" * 70)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[INFO] Application interrupted by user (Ctrl+C)")
        sys.exit(0)
