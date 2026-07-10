INPUT_FILE = "transactions.txt"
OUTPUT_FILE = "report.txt"

def read_transactions(filename):
    totals = {}
    try:
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
                
            parts = line.split(",")
            name = parts[0].strip()
            amount_str = parts[1].strip()
            amount = float(amount_str)
            
            totals[name] = totals.get(name, 0.0) + amount
            
        file.close()
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}

    return totals

def print_summary(totals):
    if not totals:
        print("No data to print.")
        return

    sorted_items = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    
    for customer, amount in sorted_items:
        print(f"{customer}: {amount:.2f}")

def write_report(totals, filename):
    if not totals:
        return

    sorted_items = sorted(totals.items(), key=lambda x: x[1], reverse=True)

    out_file = open(filename, "w")
    
    for customer, amount in sorted_items:
        out_file.write(f"{customer}: {amount:.2f}\n")
        
    out_file.close()

def main():
    totals = read_transactions(INPUT_FILE)
    print_summary(totals)
    write_report(totals, OUTPUT_FILE)

if __name__ == "__main__":
    main()