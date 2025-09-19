function togglePassword() {
    const pass_field = document.getElementById("password");
    pass_field.type = pass_field.type === "password" ? "text" : "password";
    const conform_field = document.getElementById("confirm_password");
    conform_field.type = conform_field.type === "password" ? "text" : "password";
}