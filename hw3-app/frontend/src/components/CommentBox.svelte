<script lang="js">
    let inCommentForm = $state(false);
    let { articleId } = $props();

    async function postComment(articleId) {
        let form = document.getElementById("comment-form");
        console.log(form);
        let params = new FormData(form);
        params.append("articleId", articleId);
        params.append("author", "user")

        console.log(params)

        // Written with help from this StackOverflow page: 
        // https://stackoverflow.com/questions/41431322/how-to-convert-formdata-html5-object-to-json
        let params_json = {}

        params.forEach((value, key) => params_json[key] = value);

        const response = await fetch("http://localhost:8000/api/comments", 
            {
                headers: {
                    "Content-Type": "application/json",
                },
                mode: "cors",
                method: "POST",
                body: JSON.stringify(params_json),
            }
        );
        console.log(await response.json());
    }

    function onCommentSubmit(articleId) {
        document.getElementById("comment-form").addEventListener("submit", function(e) {
            e.preventDefault();
            postComment(articleId);
        })
    }

    function onTextBoxClick() {
        inCommentForm = true;
    }

    function onCancelBtnClicked() {
        inCommentForm = false;
    }
</script>

<form id="comment-form">
    <input name="commentBody" type="text" placeholder="Share your thoughts" onclick={onTextBoxClick}>

    {#if inCommentForm}
        <button id="cancel-btn" onclick={onCancelBtnClicked} type="reset">CANCEL</button>
        <button id="submit-btn" onclick={() => {onCommentSubmit(articleId)}}>SUBMIT</button>
    {/if}
</form>