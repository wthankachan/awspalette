import { PostCard } from "@/components/post-card"

const SAMPLE_POSTS = [
  {
    id: "1",
    author: {
      name: "Sarah Chen",
      username: "@sarahchen",
      avatar: "/professional-woman.png",
    },
    content:
      "Just launched our new design system! 🎨 It's been months of work but so worth it. Check out the documentation and let me know what you think!",
    image: "/modern-design-system-interface.png",
    timestamp: "2h ago",
    likes: 234,
    comments: 45,
    shares: 12,
  },
  {
    id: "2",
    author: {
      name: "Marcus Johnson",
      username: "@marcusj",
      avatar: "/casual-man.png",
    },
    content:
      "The future of web development is here. React Server Components are changing everything we thought we knew about building apps.",
    timestamp: "4h ago",
    likes: 567,
    comments: 89,
    shares: 34,
  },
  {
    id: "3",
    author: {
      name: "Elena Rodriguez",
      username: "@elenacodes",
      avatar: "/woman-developer.png",
    },
    content: "Coffee + Code = Perfect Morning ☕️💻",
    image: "/coffee-laptop-workspace.jpg",
    timestamp: "6h ago",
    likes: 892,
    comments: 123,
    shares: 45,
  },
  {
    id: "4",
    author: {
      name: "Alex Kim",
      username: "@alexkim",
      avatar: "/person-tech.png",
    },
    content:
      'Excited to announce that I\'ll be speaking at TechConf 2025! Topic: "Building Scalable Applications with Modern Architecture". See you there! 🚀',
    timestamp: "8h ago",
    likes: 445,
    comments: 67,
    shares: 28,
  },
]

export function PostsFeed() {
  return (
    <div className="space-y-4">
      {SAMPLE_POSTS.map((post) => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  )
}
