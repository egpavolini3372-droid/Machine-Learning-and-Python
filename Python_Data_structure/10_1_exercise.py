# Program to count email messages by hour from an mbox file

def count_emails_by_hour(filename="mbox-short.txt"):
    try:
        handle = open(filename)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    counts = dict()
    for line in handle:
        # Check for lines starting with 'From ' (note the space to avoid 'From:')
        if line.startswith('From '):
            words = line.split()
            # The time is the 6th word (index 5) in the line
            time_str = words[5]
            # Extract the hour by splitting the time string by the colon
            hour = time_str.split(':')[0]
            # Increment the count for the hour in the dictionary
            counts[hour] = counts.get(hour, 0) + 1
    
    handle.close()

    # Sort the counts by hour and print the results
    for hour, count in sorted(counts.items()):
        print(hour, count)

if __name__ == "__main__":
    # Prompt user for file name, with a default for mbox-short.txt
    name = input("Enter file name (default mbox-short.txt): ")
    if len(name) < 1:
        name = "mbox-short.txt"
    count_emails_by_hour(name)
