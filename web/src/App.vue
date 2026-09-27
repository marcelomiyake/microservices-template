<script setup lang="ts">
import { onMounted, ref } from 'vue'

const message = ref('Connecting to the Rust services…')
const error = ref(false)

async function loadExample() {
  error.value = false
  message.value = 'Connecting to the Rust services…'
  try {
    const response = await fetch('/api/example')
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    const data: unknown = await response.json()
    if (typeof data !== 'object' || data === null || !('message' in data) || typeof data.message !== 'string') {
      throw new Error('Invalid response')
    }
    message.value = data.message
  } catch {
    error.value = true
    message.value = 'The example request failed. Start both Rust services and retry.'
  }
}

onMounted(loadExample)
</script>

<template>
  <main class="shell">
    <p class="eyebrow">Rust · Vue · Microservices</p>
    <h1>Start your proof of concept</h1>
    <p class="intro">This page calls the web API, which calls the example service.</p>
    <section class="result" aria-live="polite">
      <h2>Example response</h2>
      <p :class="{ error }">{{ message }}</p>
      <button v-if="error" type="button" @click="loadExample">Retry</button>
    </section>
    <p class="next">Replace this sample flow with your first bounded context. See the repository README and system design guide.</p>
  </main>
</template>
