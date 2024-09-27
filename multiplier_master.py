import requests

# List of compute node IPs
compute_nodes = [
    'http://cn1:5000/multiply',  
    'http://cn2:5000/multiply'
]

# The list of 10 integers to compute multiplication tables for
integers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def send_to_node(node_url, number):
    """Send a number to a compute node to calculate the multiplication table."""
    try:
        response = requests.post(node_url, json={'number': number})
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get response from {node_url}")
            return None
    except Exception as e:
        print(f"Error contacting {node_url}: {e}")
        return None

def distribute_work(numbers):
    """Distribute the work across compute nodes."""
    results = {}
    for i, number in enumerate(numbers):
        node_url = compute_nodes[i % len(compute_nodes)]
        print(f"Sending {number} to {node_url}")
        result = send_to_node(node_url, number)
        if result:
            results[number] = result
    return results

if __name__ == '__main__':
    print("Distributing work to compute nodes...")
    result = distribute_work(integers)
    print("Final result:", result)
