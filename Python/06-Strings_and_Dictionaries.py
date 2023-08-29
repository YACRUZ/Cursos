##Ejercicio 1
print("===== Question 1 =====")
#For our purposes, a valid zip code is any string consisting of exactly 5 digits.
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if(len(zip_code)==5 and zip_code.isdigit()):
        return True
    else: 
        return False
print(is_valid_zip([1,2,3,4]))



##Ejercicio 2
print("\n===== Question 2 =====")
#A researcher has gathered thousands of news articles.
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    return [enum for enum, x in enumerate(doc_list) if keyword.lower() in [y.rstrip('.,').lower() for y in x.split()]]
doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
print(word_search(doc_list, 'casino'))



##Ejercicio 3
print("\n===== Question 3 =====")
#Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.
def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices
doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
print(multi_word_search(doc_list, keywords))