class Pattern{

    npattern(){
        let uname = document.getElementById('su_username').value;
        const nameptn = /[A-Za-z0-9_.]+$/;
        let result = uname.match(nameptn);
        return result;

    }
    ppattern(){

        let pwd = document.getElementById('su_password').value;
        const psptn = /[A-z0-9_@!#$]+$/;
        let result = pwd.match(psptn);
        return result;
    }
}

function signup(){
    
    uname = document.getElementById('su_username').value;
    pwd = document.getElementById('su_password').value;
    cpwd = document.getElementById('su_cm_password').value;

    sessionStorage.setItem("se_username",uname);
    sessionStorage.setItem("se_password",pwd);

    const check = new Pattern();

    if(uname == ""){
        alert("Username cannot be Empty!");
    }else if(check.npattern() == null){
        alert("Username can only contain(A-Z,a-z,0-9(.)(_)");
    
    }else if (uname.length < 5 || uname.length > 15){
        alert("Username must be atleast 5 and at most 15 charaters");

    }else if(pwd == ""){
        alert("Password cannot be Empty!");

    }else if (check.ppattern() == null){
        alert("Password can contain(A-Z,a-z,0-9,_!@#$.)");

    }else if (pwd.length < 8 || pwd.length > 32){
        alert("Password must be atleast 8 and at most 32 charaters or special chars");

    }else if(cpwd == ""){
        alert("Confirm Password cannot be Empty!");

    }else if (pwd != cpwd){
        alert("'Password' and 'Confirm Password' are not Matching!");

    }else{
        alert("Signed up Successfully!");


    }
    
}
    


function login(){
    su_username = sessionStorage.getItem("se_username");
    su_password = sessionStorage.getItem("se_password");

    console.log('uname li: ',su_username);
    console.log('passwd li: ',su_password);

    li_username = document.getElementById('li_username').value;
    li_password = document.getElementById('li_password').value;

    if (li_username == su_username && li_password == su_password){

        alert("Login successfully!");

    }else{
        
        alert("Failed! Invalid 'Username' or 'Password'");
    }
}


