let newButton = document.createElement("button");

newButton.id = "btn";
newButton.innerHTML = 0;
document.body.appendChild(newButton);

let buttonText = document.getElementById("btn");
buttonText.addEventListener("click", function(){
    buttonText.innerHTML = parseInt(newButton.innerHTML) + 1;
});