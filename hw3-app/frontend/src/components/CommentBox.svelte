<script lang="js">
    let inCommentForm = $state(false);
    let { articleId } = $props();

    function postComment(articleId) {
        let params = new FormData(document.getElementById("comment-form"));
        params.append("article_id", articleId);
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
    <input name="comment_body" type="text" placeholder="Share your thoughts" onclick={onTextBoxClick}>

    {#if inCommentForm}
        <button id="cancel-btn" onclick={onCancelBtnClicked} type="reset">CANCEL</button>
        <button id="submit-btn" onclick={() => {onCommentSubmit(articleId)}}>SUBMIT</button>
    {/if}
</form>