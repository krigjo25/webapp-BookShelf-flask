<template>
  <header>
    <HeaderView />
  </header>
  <main>
    <RouterView />
  </main>
</template>

<script setup>
import { RouterView } from 'vue-router'

import HeaderView from './components/header_components/Header.vue'
</script>
