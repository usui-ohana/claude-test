// フッターの年表示
document.getElementById("year").textContent = new Date().getFullYear();

// ギャラリー: ホバーでのキャプション開示はCSSのみで実現しているが、
// タッチデバイス（ホバー不可）ではタップでキャプションの開閉を切り替える。
const galleryItems = document.querySelectorAll(".gallery-item");

galleryItems.forEach((item) => {
  item.addEventListener("click", (event) => {
    const isTouchOnly = window.matchMedia("(hover: none)").matches;
    if (!isTouchOnly) return;

    const alreadyRevealed = item.classList.contains("is-revealed");

    // 他のカードは閉じてから、対象のカードだけ開閉を切り替える
    galleryItems.forEach((other) => other.classList.remove("is-revealed"));

    if (!alreadyRevealed) {
      item.classList.add("is-revealed");
    }
  });
});
