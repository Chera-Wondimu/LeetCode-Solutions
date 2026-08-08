/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise(resolve => {
        setTimeout(resolve, millis);
    });
}
async function test() {
    console.log("Starting...");
    const start = Date.now();
    await sleep(1000);
    const end = Date.now();
    console.log("Finished!");
    console.log("Elapsed time:", end - start, "ms");
}
test();