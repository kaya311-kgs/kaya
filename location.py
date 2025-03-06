import platform
import socket
import requests
import json
from datetime import datetime

def get_system_info():
    """Get information about the user's system."""
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": socket.gethostname(),
        "Python Version": platform.python_version()
    }
    return system_info

def get_location_info():
    """Get location information based on IP address."""
    try:
        # Using ipinfo.io which provides free IP-based geolocation
        response = requests.get('https://ipinfo.io/json')
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to get location: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": f"Failed to get location: {str(e)}"}

def save_to_file(data, filename="system_location_info.txt"):
    """Save the collected information to a text file."""
    with open(filename, 'w') as file:
        file.write(f"Information collected on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        file.write("=== SYSTEM INFORMATION ===\n")
        for key, value in data["system_info"].items():
            file.write(f"{key}: {value}\n")
        
        file.write("\n=== LOCATION INFORMATION ===\n")
        for key, value in data["location_info"].items():
            file.write(f"{key}: {value}\n")
        
    print(f"Information saved to {filename}")

def main():
    # Collect information
    system_info = get_system_info()
    location_info = get_location_info()
    
    # Combine all data
    all_data = {
        "system_info": system_info,
        "location_info": location_info
    }
    
    # Save to file
    save_to_file(all_data)

if __name__ == "__main__":
    main()