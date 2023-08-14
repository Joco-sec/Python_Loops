# Run for loop with range
for i in range(5):
    print("cannot connect to destination")

# Run while loop for maximum connected devices

max_devices = 5
i = 1

while i < max_devices:
    print("User can still connect additional devices")
    i = i + 1
print("user has reached maximum number of connected devices")

# While loop in regards to login attempts

login_attempt = 0

while login_attempt < 5:
    print("login attempt:", login_attempt)
    login_attempt = login_attempt + 1
print("max login attempts reached")

# Using Boolean values in while loop for login status

login_status = True
count = 0

while login_status == True:
    print("Try again.")
    count = count + 1
    if count == 4:
        login_status = False

# Using break in a loop

computer_assets = ["Desktop1", "Smartphone03", "Laptop10"]
for asset in computer_assets:
    if asset == "Laptop10":
        break
    print(asset)

# Using 'continue' keyword to skip an iteration while using a loop

for asset in computer_assets:
    if asset == "Smartphone03":
        continue
    print(asset)

# Creating a personalized welcome message using loop

name = ["James", "Kristen", "Thomas"]

for i in name:
    print("Welcome,", i)

# Creating loop for allowed vs. not allowed IP addresses

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71",
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

for i in ip_addresses:
    if i in allow_list:
        print("IP addresse allowed")
    else:
        print("IP address not allowed")