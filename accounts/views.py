from django.shortcuts import render, redirect


# ================= REGISTER PAGE =================
def register(request):

    if request.method == "POST":
        # Get form values
        role = request.POST.get("role")   # student / instructor
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        print("User Role:", role)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)

        # Later we will save this into database
        # For now just redirect to login page
        return redirect("login")

    return render(request, "accounts/register.html")


# ================= LOGIN PAGE =================
def login_view(request):

    if request.method == "POST":
        role = request.POST.get("role")   # student / instructor
        email = request.POST.get("email")
        password = request.POST.get("password")

        print("Login Role:", role)
        print("Email:", email)

        # Later we will authenticate user
        return redirect("home")

    return render(request, "accounts/login.html")
