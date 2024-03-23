const fishies = [3,5,3,1,4,4,5,5,2,1,4,3,5,1,3,5,3,2,4,3,5,3,1,1,2,1,4,5,3,1,4,5,4,3,3,4,3,1,1,2,2,4,1,1,4,3,4,4,2,4,3,1,5,1,2,3,2,4,4,1,1,1,3,3,5,1,4,5,5,2,5,3,3,1,1,2,3,3,3,1,4,1,5,1,5,3,3,1,5,3,4,3,1,4,1,1,1,2,1,2,3,2,2,4,3,5,5,4,5,3,1,4,4,2,4,4,5,1,5,3,3,5,5,4,4,1,3,2,3,1,2,4,5,3,3,5,4,1,1,5,2,5,1,5,5,4,1,1,1,1,5,3,3,4,4,2,2,1,5,1,1,1,4,4,2,2,2,2,2,5,5,2,4,4,4,1,2,5,4,5,2,5,4,3,1,1,5,4,5,3,2,3,4,1,4,1,1,3,5,1,2,5,1,1,1,5,1,1,4,2,3,4,1,3,3,2,3,1,1,4,4,3,2,1,2,1,4,2,5,4,2,5,3,2,3,3,4,1,3,5,5,1,3,4,5,1,1,3,1,2,1,1,1,1,5,1,1,2,1,4,5,2,1,5,4,2,2,5,5,1,5,1,2,1,5,2,4,3,2,3,1,1,1,2,3,1,4,3,1,2,3,2,1,3,3,2,1,2,5,2];
const fishies1 = [3,4,3,1,2];
function total_days(day, fishList) {
	const fishMap = {};
	fishList.forEach(f => {
		if (fishMap[f]) {
			fishMap[f] += 1;
		} else {
			fishMap[f] = 1;
		}
	});
	console.log(fishMap)
	let total = 0;
	// Object.keys(fishMap).forEach(async (fish) => {
	// 	const single_fish_total = single_fish_days(day, fish);
	// 	console.log(fish)
	// 	console.log(single_fish_total)
	// 	total += single_fish_total * fishMap[fish];
	// });
	total += single_fish_days(day, 3)// * fishMap[fish];
	console.log(total);
}

total_days(18, fishies1);
// total_days(80, fishies1);

function single_fish_days(day, fish) {
	let dayCount = parseInt(fish)+1;
	let fishList = [6, 8];
	let newFish = [];
	while (dayCount < day) {
		console.log("Day:" + dayCount)
		let newNewFish = [];
		for (let i = 0; i < newFish.length; i += 1) {
			if (newFish[i] != 0) {
				newFish[i] = newFish[i] - 1
			} else {
				newFish[i] = 6;
				newNewFish.push(8);
			}
		}
		if (newNewFish.length > 0) {
			newFish = newFish.concat(newNewFish);
		}
		for (let i = 0; i < fishList.length; i += 1) {
			if (fishList[i] != 0) {
				fishList[i] = fishList[i] - 1
			} else {
				fishList[i] = 6;
				newFish.push(8);
			}
		}
		dayCount += 1;

	}
	console.log(fishList.length + newFish.length)
	return fishList.length + newFish.length;
}