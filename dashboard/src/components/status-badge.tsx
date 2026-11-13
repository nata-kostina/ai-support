import { Badge } from "@/components/ui/badge"

export type EventStatus =
    | 'processing'
    | 'processed'
    | 'skipped'
    | 'failed'
    | 'open'
    | 'answered'
    | 'escalated';

interface StatusBadgeProps {
    status: EventStatus | string;
}

export function StatusBadge({ status }: StatusBadgeProps) {
    const getConfig = (s: string) => {
        switch (s) {
            case 'processing':
                return { label: 'Processing', className: 'bg-blue-500/10 text-blue-500 hover:bg-blue-500/20 border-blue-500/20' };
            case 'processed':
                return { label: 'Processed', className: 'bg-emerald-500/10 text-emerald-500 hover:bg-emerald-500/20 border-emerald-500/20' };
            case 'skipped':
                return { label: 'Skipped', className: 'bg-zinc-500/10 text-zinc-500 hover:bg-zinc-500/20 border-zinc-500/20' };
            case 'failed':
                return { label: 'Failed', className: 'bg-destructive/10 text-destructive hover:bg-destructive/20 border-destructive/20' };

            // Вторая группа (жизненный цикл тикета / события)
            case 'open':
                return { label: 'Open', className: 'bg-amber-500/10 text-amber-500 hover:bg-amber-500/20 border-amber-500/20' };
            case 'answered':
                return { label: 'Answered', className: 'bg-emerald-500/10 text-emerald-500 hover:bg-emerald-500/20 border-emerald-500/20' };
            case 'escalated':
                return { label: 'Escalated', className: 'bg-purple-500/10 text-purple-500 hover:bg-purple-500/20 border-purple-500/20' };

            default:
                return { label: s, className: 'bg-secondary text-secondary-foreground' };
        }
    };

    const config = getConfig(status);

    return (
        <Badge variant="outline" className={`font-medium capitalize ${config.className}`}>
            {config.label}
        </Badge>
    );
}