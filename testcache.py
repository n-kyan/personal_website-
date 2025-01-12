from calendar_source import OutlookCalendar
from datetime import datetime
import os

def test_caching():
    print("\nTesting calendar authentication and caching...")
    
    # Check if cache file exists before starting
    cache_exists = os.path.exists(".token_cache.json")
    print(f"Token cache file exists before test: {cache_exists}")
    
    try:
        calendar = OutlookCalendar()
        today = datetime.now().date()
        
        print("\nAttempting to get available slots...")
        available_slots = calendar.get_available_slots(today)
        
        # Check if cache file was created/updated
        cache_exists_after = os.path.exists(".token_cache.json")
        print(f"\nToken cache file exists after test: {cache_exists_after}")
        
        if available_slots:
            print("\nAvailable time slots:")
            for slot in available_slots:
                print(f"{slot['start']} - {slot['end']}")
        else:
            print("\nNo available slots found for today")

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    test_caching()
    
    # Let user test multiple runs
    while True:
        response = input("\nWould you like to test again to verify caching? (y/n): ")
        if response.lower() != 'y':
            break
        print("\n--- Running test again ---")
        test_caching()