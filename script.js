function gameOpened(){
	document.getElementById("popuptext").innerHTML = "If you lost the game, don't be discouraged. You were meant to lose. So why did you lose the game? One committed person is not enough to fight against pollution. We need people to band together and stop pollution before it becomes too late.That is the purpose of this website. So share with all your friends and do your part to reduce pollution.";
	document.getElementById("popupimage").style.display = "block";
}

var popup = document.getElementById("popup");
var btn = document.getElementById("x");
setTimeout(function(){popup.style.display="block";}, 5000);
btn.onclick = function(){popup.style.display="none";}
