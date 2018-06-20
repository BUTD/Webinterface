var DataCache = function(numberOfFields, cacheSize){
	this.cacheSize = cacheSize;
	this.numberOfFields = numberOfFields
	this.cache = [];
	for (var id=0;id<numberOfFields;id++){
		this.cache.push([]);
	}
}

DataCache.prototype.addNumbers = function(numbers){
	for (var id=0; id<this.cache.length; id++){
		this.cache[id].push(numbers[id])
	}
	if (this.cache[0].length >= this.cacheSize){
		return true;
	}
	else{
		return false;
	}
}

DataCache.prototype.getAveragesAndClear = function(){
	var averages = [];
	var len = 0;
	// calculate averages and store in array averages
	for (var id=0; id<this.cache.length; id++){
		len = this.cache[id].length;
		averages.push(
				this.cache[id].reduce(function(acc, val) { return acc + val; })/len);
	}
	// clear cache
	this.cache = [];
	for (var id=0;id<this.numberOfFields;id++){
		this.cache.push([]);
	}
	// return result
	return averages;
}

//var c = new DataCache(3,20);
//var numbers = [1,2,3];
//c.addNumbers(numbers);
//numbers = [2,3,4];
//c.addNumbers(numbers);
//c.addNumbers(numbers);
//console.log(c.getAveragesAndClear());

//
//var test = [new DataCache(2,2),new DataCache(3,2), new DataCache(4,5)]
//test[1].addNumbers([1,2,3])
//console.log(test[1].cache)
