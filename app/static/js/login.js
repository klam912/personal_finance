// Initialize number of attempts before locking user out (i.e., moving them to the home page)
var max_attempts = 5;

function validate_cred() {
    var user_name = document.getElementById("user-name").value;
    var pwd = document.getElementById("password").value;

    // Test creds (make sure to get it from the user database)
    if (user_name == "klam" && pwd == "123") {
        alert("Login successfully!");
        window.location = "/dashboard"; // redirect to dashboard main page
        return false;
    } else {
        max_attempts--; 
        alert("You have " + max_attempts + " attempts left!");
        if (max_attempts == 0) {
            alert("Login failed");
            // redirect to welcome page
            window.location = "/"
            return false;
        }

    }
}