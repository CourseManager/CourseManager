window.onload = function () {
    let verifyCode = new GVerify("v_container");

    document.getElementById("my_button").onclick = function () {
        function verify() {
            window.setInterval(function () {
                let res = verifyCode.validate(document.getElementById("code_input").value);
                if (res){

                } else {

                }
            },200);
        }
    }
};