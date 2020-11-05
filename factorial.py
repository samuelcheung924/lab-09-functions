def factorial(n):
    total = 1
    for i in range(1, n+1):
        #print(i)
        total = total * (i)
    return total

num = int(input("Please enter a number "))
print(num,"! is ",factorial(num))



#function factorial(n) {
#var total = 1;
#for (i = 0; i < n; i++) {
#total = total * (n - i);
#document.write(" Current i is " + i+ "<br>");
#document.write("Current value of total is " + total+ "<br>");
#// First time total = 1
#// incremenet total up to n
#}
#return total;
#// return the final value of total
#}

#var userstring = prompt("Number please:");
#var usernum = parseInt(userstring);
#document.write(usernum + "! is " + factorial(usernum));
