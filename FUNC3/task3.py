def exam (grades):
    limit = grades[0]
    marks = grades[1:]
    num = 0
    for mark in marks:
        if (mark >= limit):
            num += 1
    return (f"Exam wad passed by {num} students")
            
print (exam(input()))
    
