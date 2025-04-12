document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("quiz-form");

    // Odeslání kvízu
    form?.addEventListener("submit", () => {
        document.getElementById("result-box")?.classList.add("fade-in");
    });

    // Kliknutí na odpověď
    document.querySelectorAll(".question-block").forEach(block => {
        const radios = block.querySelectorAll("input[type='radio']");
        radios.forEach(radio => {
            radio.addEventListener("change", () => {
                block.classList.add("highlight");
                setTimeout(() => block.classList.remove("highlight"), 500);
            });
        });
    });
});
