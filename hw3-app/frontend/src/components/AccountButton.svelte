<script>
    let logged_in = $state(false);

    async function onLoginPressed() {
        const res = await fetch("http://localhost:8000/login");
        logged_in = true;
    }
</script>

{#if logged_in}
    <p>Account</p>
{:else}
    <button onclick={onLoginPressed}>LOG IN</button>
{/if}
