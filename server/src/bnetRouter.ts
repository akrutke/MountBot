import Router, { NextFunction, Request, Response } from 'express'
import passport from 'passport'


export default Router()
    .get('/oauth',passport.authenticate('bnet'))
    .get('/oauth/callback', (req:Request, res: Response, next: NextFunction) => {
        console.log('hitting callback - authenticating next')
        next()
    },
    passport.authenticate('bnet'),
    function(req: Request, res: Response) {
        res.sendStatus(200)
    });