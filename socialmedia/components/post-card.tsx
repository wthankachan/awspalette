import { Heart, MessageCircle, Share2, MoreHorizontal } from "lucide-react"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card"

interface Post {
  id: string
  author: {
    name: string
    username: string
    avatar: string
  }
  content: string
  image?: string
  timestamp: string
  likes: number
  comments: number
  shares: number
}

export function PostCard({ post }: { post: Post }) {
  return (
    <Card className="overflow-hidden">
      <CardHeader className="flex flex-row items-start gap-3 space-y-0 pb-3">
        <Avatar className="h-10 w-10">
          <AvatarImage src={post.author.avatar || "/placeholder.svg"} alt={post.author.name} />
          <AvatarFallback>{post.author.name[0]}</AvatarFallback>
        </Avatar>
        <div className="flex-1 space-y-1">
          <div className="flex items-center justify-between">
            <div>
              <p className="font-semibold leading-none">{post.author.name}</p>
              <p className="text-sm text-muted-foreground">{post.author.username}</p>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-sm text-muted-foreground">{post.timestamp}</span>
              <Button variant="ghost" size="icon" className="h-8 w-8">
                <MoreHorizontal className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </div>
      </CardHeader>
      <CardContent className="space-y-3 pb-3">
        <p className="text-sm leading-relaxed">{post.content}</p>
        {post.image && (
          <div className="overflow-hidden rounded-lg">
            <img src={post.image || "/placeholder.svg"} alt="Post content" className="w-full object-cover" />
          </div>
        )}
      </CardContent>
      <CardFooter className="flex items-center justify-between border-t border-border pt-3">
        <Button variant="ghost" size="sm" className="gap-2">
          <Heart className="h-4 w-4" />
          <span className="text-sm">{post.likes}</span>
        </Button>
        <Button variant="ghost" size="sm" className="gap-2">
          <MessageCircle className="h-4 w-4" />
          <span className="text-sm">{post.comments}</span>
        </Button>
        <Button variant="ghost" size="sm" className="gap-2">
          <Share2 className="h-4 w-4" />
          <span className="text-sm">{post.shares}</span>
        </Button>
      </CardFooter>
    </Card>
  )
}
