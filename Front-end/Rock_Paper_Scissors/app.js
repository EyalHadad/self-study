let userScore = 0; //use for the scores
let compScore = 0; 
const smallUserWord = "user".fontsize(3).sub(); //.sub() locate it under the line, sup() locate it on top of the line
const smallCompWord = "comp".fontsize(3).sub();
const userScore_span = document.getElementById("user-score"); // get elment by his ID
const compScore_span = document.getElementById("computer-score");
const scoreBoard_div = document.querySelector(".score-board"); //get an element when you don't have the id
const result_p = document.querySelector(".result > p "); //get the p tag in the result div
const rock_div = document.getElementById("r");
const paper_div = document.getElementById("p");
const scissors_div = document.getElementById("s");


function getComputerChoice() {
	const choices = ['r','p','s'];
	return choices[Math.floor(Math.random() * 3)];
}

function convertToWord(l) {
	if(l=='r') return "Rock";
	if(l=='p') return "Paper";
	return "Scissor";
}



function win(userChoice, compChoice) {
	userScore++;
	userScore_span.innerHTML = userScore; // innerHTML Change the HTML content
	result_p.innerHTML = convertToWord(userChoice) + smallUserWord + " beats " + convertToWord(compChoice)+ smallCompWord + " .You Win!";
	document.getElementById(userChoice).classList.add('green-glow');
	// ClassList returns a live DOMTokenList collection of the class attributes of the element.
	setTimeout(function() {document.getElementById(userChoice).classList.remove('green-glow')}, 300);
	// SetTimeout define a time that after that to execute the operation.
}

function loss(userChoice, compChoice) {
	compScore++;
	compScore_span.innerHTML = compScore; // innerHTML Change the HTML content
	result_p.innerHTML = convertToWord(compChoice) + smallCompWord+ " beats " + convertToWord(userChoice) + smallUserWord + " .You Lost...";
	document.getElementById(userChoice).classList.add('red-glow');
	setTimeout(function() {document.getElementById(userChoice).classList.remove('red-glow')}, 300);
}

function draw(userChoice, compChoice) {
	result_p.innerHTML = convertToWord(userChoice) + smallUserWord  + " and " + convertToWord(compChoice)+ smallCompWord + " .its Draw!";
	document.getElementById(userChoice).classList.add('gray-glow');
	setTimeout(function() {document.getElementById(userChoice).classList.remove('gray-glow')}, 300);
}


function game(userChoice) {
	compChoice = getComputerChoice();
	switch (userChoice+compChoice){
		case "rs":
		case "pr":
		case "sp":
			win(userChoice,compChoice);
			break;
		case "sr":
		case "rp":
		case "ps":
			loss(userChoice,compChoice);
			break;
		default:
			draw(userChoice,compChoice);
			break;
	}
}

function main() {
	rock_div.addEventListener('click', function() { // function for click events
		game("r");
	})

	paper_div.addEventListener('click', function() { // function for click events
		game("p");
	})

	scissors_div.addEventListener('click', function() { // function for click events
		game("s");
	})

}
main();