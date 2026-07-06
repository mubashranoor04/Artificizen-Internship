import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sys as system_sys  
from src.manager import Library
from src.exceptions import LibraryError

def show_menu():
    print("   \nLIBRARY MANAGEMENT ECOSYSTEM (CLI)\n")
    
    print("1. Add a Book Portfolio")
    print("2. Register a New Member")
    print("3. Query/Search Books")
    print("4. Issue Book (Checkout)")
    print("5. Return a Book")
    print("6. Show Database Status Snapshot")
    print("7. Exit System")

def main():
    library = Library()
    
    while True:
        show_menu()
        choice = input("Select operation choice [1-7]: ").strip()
        
        try:
            if choice == "1":
                print("\n--- Add Book ---")
                title = input("Enter Title: ").strip()
                author = input("Enter Author: ").strip()
                isbn = input("Enter ISBN code: ").strip()
                copies = input("Enter Number of Copies (Default 1): ").strip()
                
                qty = int(copies) if copies.isdigit() else 1
                if not title or not author or not isbn:
                    print("Logic Error: Fields cannot be left completely empty.")
                    continue
                library.add_book(title, author, isbn, qty)
                print(f"Success: Added {qty} copy/ies of '{title}'.")

            elif choice == "2":
                print("\n--- Register Member ---")
                name = input("Enter Full Name: ").strip()
                member_id = input("Assign Unique Member ID: ").strip()
                if not name or not member_id:
                    print("Logic Error: Fields cannot be left completely empty.")
                    continue
                library.register_member(name, member_id)
                print(f"Success: Member '{name}' registered under ID: {member_id}.")

            elif choice == "3":
                print("\n--- Search Books ---")
                query = input("Enter query keyword (Title / Author / ISBN): ").strip()
                results = library.search_book(query)
                if not results:
                    print("No records matching your criteria were found.")
                else:
                    print(f"\nFound ({len(results)}) matching results:")
                    for idx, book in enumerate(results, 1):
                        print(f"  {idx}. {book}")

            elif choice == "4":
                print("\n--- Issue Book (Checkout) ---")
                m_id = input("Enter Member ID: ").strip()
                isbn = input("Enter Book ISBN: ").strip()
                library.issue_book(m_id, isbn)
                print("Success: Book checked out and logged transaction status.")

            elif choice == "5":
                print("\n--- Return Book ---")
                m_id = input("Enter Member ID: ").strip()
                isbn = input("Enter Book ISBN: ").strip()
                library.return_book(m_id, isbn)
                print("Success: Inventory tracking adjusted. Return processing complete.")

            elif choice == "6":
                print("\n=== SYSTEM SNAPSHOT STATUS ===")
                print(f"\nTotal Tracked Unique Books: {len(library.books)}")
                for book in library.books.values():
                    print(f" - {book}")
                print(f"\nTotal Registered Members: {len(library.members)}")
                for member in library.members.values():
                    print(f" - {member}")

            elif choice == "7":
                print("\nShutting down core engine threads. Goodbye!")
                sys.exit(0)
            else:
                print("Error: Invalid command select option out of range [1-7].")
                
        except LibraryError as error_msg:
            print(f"\n[Transaction Aborted]: {error_msg}")
        except Exception as e:
            print(f"\n[Fatal Core Crash Avoided]: An unexpected event occurred: {e}")

if __name__ == "__main__":
    main()