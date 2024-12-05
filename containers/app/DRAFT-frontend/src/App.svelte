<script>
  export let name;
  import { Router, Route } from "svelte-routing";
  import PostMessage from "./PostMessage.svelte";
  import SplitFlap from "./SplitFlap.svelte";
  import {
    Navbar,
    NavBrand,
    NavLi,
    NavUl,
    NavHamburger,
  } from "flowbite-svelte";
</script>

<Navbar>
  <NavBrand href="/">
    <img
      src="/images/flowbite-svelte-icon-logo.svg"
      class="me-3 h-6 sm:h-9"
      alt="Flowbite Logo"
    />
    <span
      class="self-center whitespace-nowrap text-xl font-semibold dark:text-white"
      >{name}</span
    >
  </NavBrand>
  <NavHamburger />
  <NavUl>
    <NavLi href="/">Home</NavLi>
    <NavLi href="/post">Post</NavLi>
  </NavUl>
</Navbar>

<Router>
  <Route path="/" component={SplitFlap} />
  <Route path="/post" component={PostMessage} />
</Router>