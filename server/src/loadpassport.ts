import { PassportStatic } from 'passport'
import { Strategy as BnetStrategy } from 'passport-bnet'

export default (passport: PassportStatic) => {
    passport.use('bnet',
    new BnetStrategy({
        clientID: 'b3bb0ce94dfb433b9265c458deabb736',
        clientSecret: 'Yrkrv2wviRmZwla9hgURwkNi8bZfR1SZ',
        callbackURL: "http://localhost:8080/proxy/bnet/oauth/callback",
        region: "us"
    }, function(accessToken: string, refreshToken: string, profile: any, done: any) {
        console.log(profile)
        return done(null, profile);
    }));
}



