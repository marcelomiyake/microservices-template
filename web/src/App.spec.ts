import { flushPromises, mount } from '@vue/test-utils'
import { afterEach, describe, expect, it, vi } from 'vitest'
import App from './App.vue'

afterEach(() => vi.unstubAllGlobals())

describe('example request', () => {
  it('shows the response from the browser API', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response(JSON.stringify({ message: 'hello' }))))
    const wrapper = mount(App)
    await flushPromises()

    expect(wrapper.get('[aria-live="polite"]').text()).toContain('hello')
    expect(wrapper.find('button').exists()).toBe(false)
    wrapper.unmount()
  })

  it('shows a recoverable error and retries', async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(new Response(null, { status: 502 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ message: 'recovered' })))
    vi.stubGlobal('fetch', fetchMock)
    const wrapper = mount(App)
    await flushPromises()

    expect(wrapper.get('[aria-live="polite"]').text()).toContain('request failed')
    await wrapper.get('button').trigger('click')
    await flushPromises()
    expect(wrapper.get('[aria-live="polite"]').text()).toContain('recovered')
    expect(fetchMock).toHaveBeenCalledTimes(2)
    wrapper.unmount()
  })

  it('rejects a malformed success body', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response(JSON.stringify({ message: 42 }))))
    const wrapper = mount(App)
    await flushPromises()

    expect(wrapper.get('[aria-live="polite"]').text()).toContain('request failed')
    wrapper.unmount()
  })
})
