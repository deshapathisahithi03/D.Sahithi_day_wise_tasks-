def process_test_case():
    N, Q = map(int, input().split())  # Read N (number of friends) and Q (queries)
    friends_dict = {}

    # Store friend details
    for i in range(N):
        name, age, hobby, fav_choc = input().split()
        friends_dict[name] = (age, hobby, fav_choc)

    # Process queries
    for i in range(Q):
        query_name = input()
        if query_name in friends_dict:
            print(*friends_dict[query_name])  # Unpack tuple and print values
        else:
            print("Friend not found")  # Handle edge case (if required)

def main():
    T = int(input().strip())  # Read number of test cases
    for i in range(T):
        process_test_case()

main()
