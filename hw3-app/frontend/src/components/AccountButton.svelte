<script>
    let logged_in = $state(false);

    async function onLoginPressed() {
        const res = await fetch("/login");
        const res_data = await res.json();
        console.log(res_data);
        logged_in = true;
    }
</script>

{#if logged_in}
    <p>Account</p>
{:else}
    <button onclick={onLoginPressed}>LOG IN</button>
{/if}
