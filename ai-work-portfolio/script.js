"use strict";

/**
 * フッターの著作権表示に現在の年をセットする。
 * @returns {void}
 */
function renderFooterYear() {
  /** @type {HTMLElement | null} */
  const yearEl = document.getElementById("year");
  if (!yearEl) return;
  yearEl.textContent = String(new Date().getFullYear());
}

/**
 * タッチデバイス（hover不可）向けに、タップでキャプションの開閉を切り替える。
 * ホバー可能なデバイスではCSSの :hover / :focus-within だけで開閉するため、
 * ここでは押下時に限り isTouchOnly を判定してリスナーの中身を分岐させる。
 * @param {NodeListOf<Element>} items - `.gallery-item` 要素の一覧
 * @returns {void}
 */
function setupTouchCaptionToggle(items) {
  items.forEach((item) => {
    item.addEventListener("click", () => {
      const isTouchOnly = window.matchMedia("(hover: none)").matches;
      if (!isTouchOnly) return;

      const alreadyRevealed = item.classList.contains("is-revealed");

      // 他のカードは閉じてから、対象のカードだけ開閉を切り替える
      items.forEach((other) => other.classList.remove("is-revealed"));

      if (!alreadyRevealed) {
        item.classList.add("is-revealed");
      }
    });
  });
}

renderFooterYear();
setupTouchCaptionToggle(document.querySelectorAll(".gallery-item"));
