students = {
    "Praveen Kumar","Pavan Adithya","Sam Snigdha","Abhi Singh",
    "Utkarsh Mishra","Chava Kethan","Praveen Yadav","Sai Urla","avan Reddy",
    "Abhinav Verma","Rohit Sharma","Rahul Kumar","Neha Singh","Ankit Mishra",
    "Aman Gupta","Sneha Patel","Kunal Mehta","Vikas Yadav","Suresh Kumar","Ravi Verma"

}

name_dict = { }
print("students with same name but different surname:\n")

for full_name in students:
    #split full name into words
    parts = full_name.split(" ")

#slicing to get first name and surname
    first_name = parts[0] 
    surname = parts[1]

#add surname to dict using set
    if first_name in name_dict:
        name_dict[first_name].add(surname)

        if len(name_dict[first_name]) == 2:

#print the nsme with more than one surname
            print(first_name, "->",",".join(name_dict[first_name]))
    else:
        name_dict[first_name] = {surname}
                                          


