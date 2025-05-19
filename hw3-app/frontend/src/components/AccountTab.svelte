<script lang="js">
    import { getContext } from "svelte";

    let {onExitClick, onLogoutClick} = $props();
    const user = getContext("userEmail");
</script>

<section class="account-tab">
    <div id="account-tab-top">
        <button class="exit-button" onclick={onExitClick}>×</button>
        <h2>{user}</h2>
        <p>Good afternoon.</p>
    </div>
    <button id="log-out-button" onclick={onLogoutClick}>Log out</button>
</section>