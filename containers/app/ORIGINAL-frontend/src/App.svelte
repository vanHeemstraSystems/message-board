<script>
  import { Router, Route, Link } from "svelte-routing";
  import SplitFlap from "./SplitFlap.svelte";
  import PostMessage from "./PostMessage.svelte";
</script>

<nav class="flex justify-between p-4 bg-gray-800 text-white">
  <Link to="/" class="hover:underline">Split Flap Display</Link>
  <Link to="/post" class="hover:underline">Post Message</Link>
</nav>

<Router>
  <Route path="/" component={SplitFlap} />
  <Route path="/post" component={PostMessage} />
</Router>

<style>
  nav {
    background-color: #2d3748;
  }
</style>
