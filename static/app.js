
document.getElementById("copy-btn").addEventListener("click", function() {
    let password = document.getElementById("password");
    let range = document.createRange();
    range.selectNode(password);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand("copy");
    alert("Password copied to clipboard");
});
