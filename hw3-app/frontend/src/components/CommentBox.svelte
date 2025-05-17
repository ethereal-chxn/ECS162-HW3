<script>
    let inCommentForm = $state(false);

    function postComment() {
        let params = new FormData(id("comment-form"));
        params.append()
    }

    function onCommentSubmit() {
        id("comment-form").addEventListener("submit", function(e) {
            e.preventDefault();
            postComment();
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
    Comment Body: <input name="comment-body" type="text" placeholder="Share your thoughts" on:click={onTextBoxClick}>

    {#if inCommentForm}
        <button id="cancel-btn" on:click={onCancelBtnClicked} type="reset">CANCEL</button>
        <button id="submit-btn" on:click={onCommentSubmit}>SUBMIT</button>
    {/if}
</form>