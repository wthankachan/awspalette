import { Header } from "@/components/header"
import { PostsFeed } from "@/components/posts-feed"
import { ChatSidebar } from "@/components/chat-sidebar"

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <div className="flex">
        <main className="flex-1 max-w-3xl mx-auto px-4 py-6">
          <PostsFeed />
        </main>
        <aside className="hidden lg:block w-80 border-l border-border">
          <ChatSidebar />
        </aside>
      </div>
    </div>
  )
}
