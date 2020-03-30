function messageUser(){
	var full = window.location.href;
	var split = full.indexOf('/', 9)+1;
	var rHalf = full.substr(split, full.length);
	split = rHalf.indexOf('/');
	var account = rHalf.substr(0, split);
	var url = "/m/messages/compose/"+account
	return url;
	
}