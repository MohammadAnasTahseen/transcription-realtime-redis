import time

def testing(lst, tar):
    print(f"passed numbers here are these {lst},{tar}")
    start_time = time.perf_counter()  # Start the high precision timer

    for i in range(len(lst)):
        if lst[i] == tar:  # If target is found
            print("number found at", i)
            end_time = time.perf_counter()  # End the high precision timer
            elapsed_time = (end_time - start_time) * 1000  # Calculate elapsed time in milliseconds
            return "number found", lst[i], elapsed_time
    
    return "number not found"

# Sample list and target
array = [1, 2, 3, 10, 5, 6, 5, 6, 7, 8, 9, 10, 4, 3, 2, 112]
target = 1

# Call the function
a = testing(array, target)
print("returned  ", a)


# import time

# def find_target(input_list, target):

#     if not input_list:  # Early return for empty list
#         return "number not found", None, 0.0

#     start_time = time.perf_counter()  # Start the high precision timer
#     length=len(input_list)
#     print("#########################",length)

#     for i, value in enumerate(input_list):
#         if value== target:
#             end_time = time.perf_counter()  # End the high precision timer
#             elapsed_time = (end_time - start_time) * 1000  # Time in milliseconds
#             return "number found", value, elapsed_time,f"at {i}"
    
#     return "number not found", None, 0.0  # Return None if not found






# if __name__ == "__main__":
#     array = [0, 2, 3, 10, 5, 6, 5, 6, 7, 8, 9, 10, 4, 3, 2, 112]
#     target = 2

#     result, value, time_taken, location = find_target(array, target)
    
#     print(f"Returned: {result}")
#     if result == "number found":
#         print(f"Target value: {value}, Time taken: {time_taken:.6f} ms, Location: {location}")
#     else:
#         print("Target not found.")


# import time

# class TargetFinder:
#     def __init__(self, input_list):
#         """
#         Initializes the TargetFinder class with an input list.
#         Args:
#         input_list (list): The list to search through.
#         """
#         self.input_list = input_list

#     def find_target(self, target):
#         """
#         Searches for a target number in the list and returns the result along with the time taken to search.

#         Args:
#         target (int): The number to find in the list.

#         Returns:
#         tuple: A message indicating whether the target was found, the target value (if found), 
#                the time in milliseconds, and the location (index) in the list if found.
#         """
#         if not self.input_list:  # Early return for empty list
#             return "number not found", None, 0.0, None

#         start_time = time.perf_counter()  # Start the high precision timer
#         length = len(self.input_list)
#         print("#########################", length)

#         for i, value in enumerate(self.input_list):
#             if value == target:
#                 end_time = time.perf_counter()  # End the high precision timer
#                 elapsed_time = (end_time - start_time) * 1000  # Time in milliseconds
#                 return "number found", value, elapsed_time, f"at {i}"
        
#         return "number not found", None, 0.0, None  # Return None if not found


# if __name__ == "__main__":
#     array = [0, 2, 3, 10, 5, 6, 5, 6, 7, 8, 9, 10, 4, 3, 2, 112]
#     target = 2

#     finder = TargetFinder(array)  # Instantiate the class with the input list
#     result, value, time_taken, location = finder.find_target(target)
    
#     print(f"Returned: {result}")
#     if result == "number found":
#         print(f"Target value: {value}, Time taken: {time_taken:.6f} ms, Location: {location}")
#     else:
#         print("Target not found.")





# python -m celery -A celery_project worker --pool=threads --loglevel=info