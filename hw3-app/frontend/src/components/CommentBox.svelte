<script>
    let inCommentForm = $state(false);
    let articleId = $props();

    function postComment(articleId) {
        let params = new FormData(id("comment-form"));
        params.append("article_id", articleId);
    }

    function onCommentSubmit(articleId) {
        id("comment-form").addEventListener("submit", function(e) {
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
    <input name="comment_body" type="text" placeholder="Share your thoughts" on:click={onTextBoxClick}>

    {#if inCommentForm}
        <button id="cancel-btn" on:click={onCancelBtnClicked} type="reset">CANCEL</button>
        <button id="submit-btn" on:click={onCommentSubmit, articleId}>SUBMIT</button>
    {/if}
</form>