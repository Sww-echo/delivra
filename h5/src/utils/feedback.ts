import { showConfirmDialog as showVantConfirmDialog, showToast } from 'vant'

export function showSubmitSuccess(message = '提交成功') {
  showToast({ type: 'success', message })
}

export async function showConfirmDialog(message: string, title = '确认操作') {
  await showVantConfirmDialog({ title, message })
}

export async function copyText(text: string, message = '已复制') {
  if (navigator.clipboard) {
    await navigator.clipboard.writeText(text)
  }
  showToast(message)
}
