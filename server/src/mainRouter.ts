import bnetRouter from './bnetRouter'
import Router, { Request, Response } from 'express'

export default Router()
    .get('/health', (req: Request, res: Response) => {res.sendStatus(200)})
    .use('/bnet', bnetRouter)