import { Search } from "lucide-react"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"

const SAMPLE_CHATS = [
  {
    id: "1",
    name: "Jessica Park",
    username: "@jessicap",
    avatar: "/diverse-woman-smiling.png",
    lastMessage: "That sounds great! Let's do it",
    timestamp: "2m",
    unread: 2,
    online: true,
  },
  {
    id: "2",
    name: "David Miller",
    username: "@davidm",
    avatar: "/professional-man.png",
    lastMessage: "Thanks for the help!",
    timestamp: "15m",
    unread: 0,
    online: true,
  },
  {
    id: "3",
    name: "Lisa Anderson",
    username: "@lisaa",
    avatar: "/casual-woman.png",
    lastMessage: "See you tomorrow 👋",
    timestamp: "1h",
    unread: 0,
    online: false,
  },
  {
    id: "4",
    name: "Ryan Cooper",
    username: "@ryanc",
    avatar: "/man-tech.png",
    lastMessage: "Did you check the latest update?",
    timestamp: "3h",
    unread: 1,
    online: false,
  },
  {
    id: "5",
    name: "Emma Wilson",
    username: "@emmaw",
    avatar: "/woman-developer.png",
    lastMessage: "Perfect! I'll send it over",
    timestamp: "5h",
    unread: 0,
    online: true,
  },
  {
    id: "6",
    name: "Tom Harris",
    username: "@tomh",
    avatar: "/casual-man.png",
    lastMessage: "Sounds good to me",
    timestamp: "1d",
    unread: 0,
    online: false,
  },
]

export function ChatSidebar() {
  return (
    <div className="flex h-[calc(100vh-4rem)] flex-col">
      <div className="border-b border-border p-4">
        <h2 className="mb-3 text-lg font-semibold">Messages</h2>
        <div className="relative">
          <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
          <Input placeholder="Search messages..." className="pl-9 bg-muted/50 border-0" />
        </div>
      </div>
      <ScrollArea className="flex-1">
        <div className="space-y-1 p-2">
          {SAMPLE_CHATS.map((chat) => (
            <Button key={chat.id} variant="ghost" className="w-full justify-start gap-3 h-auto py-3 px-3">
              <div className="relative">
                <Avatar className="h-10 w-10">
                  <AvatarImage src={chat.avatar || "/placeholder.svg"} alt={chat.name} />
                  <AvatarFallback>{chat.name[0]}</AvatarFallback>
                </Avatar>
                {chat.online && (
                  <span className="absolute bottom-0 right-0 h-3 w-3 rounded-full bg-accent border-2 border-card" />
                )}
              </div>
              <div className="flex-1 text-left space-y-1">
                <div className="flex items-center justify-between">
                  <p className="text-sm font-medium leading-none">{chat.name}</p>
                  <span className="text-xs text-muted-foreground">{chat.timestamp}</span>
                </div>
                <div className="flex items-center justify-between">
                  <p className="text-xs text-muted-foreground line-clamp-1">{chat.lastMessage}</p>
                  {chat.unread > 0 && (
                    <span className="flex h-5 w-5 items-center justify-center rounded-full bg-primary text-xs font-medium text-primary-foreground">
                      {chat.unread}
                    </span>
                  )}
                </div>
              </div>
            </Button>
          ))}
        </div>
      </ScrollArea>
      <div className="border-t border-border p-4">
        <div className="relative overflow-hidden rounded-lg bg-gradient-to-br from-primary/20 to-accent/20 p-4">
          <div className="relative z-10 space-y-2">
            <p className="text-sm font-medium text-balance leading-relaxed">Find the new you by losing yourself...</p>
          </div>
          <div className="mt-3">
            <img
              src="shoes-updated.png"
              alt="Athletic shoes advertisement"
              className="w-full h-auto rounded-md"
            />
          </div>
        </div>
      </div>
    </div>
  )
}
