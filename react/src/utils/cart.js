export default function countItemsInCart(cart) {
    let totalItems = 0;

    for (let item in cart["quantities"]) {
        totalItems += cart["quantities"][item]
    }

    return totalItems;
}