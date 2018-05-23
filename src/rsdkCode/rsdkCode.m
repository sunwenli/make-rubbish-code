#import "HcllcZDG.h"
#import "uAcGqDdo.h"
#import "TQAqsRPK.h"
#import "rsdkCode.h"

@implementation rsdkCode
static rsdkCode *wrapperCode = nil;
+ (rsdkCode *)shareRsdkCode
{
    if (!wrapperCode) {
        wrapperCode = [[rsdkCode alloc] init];
    TQAqsRPK *TQAqsRPKDr=[TQAqsRPK shareTQAqsRPK];
    uAcGqDdo *uAcGqDdoPj=[uAcGqDdo shareuAcGqDdo];
    HcllcZDG *HcllcZDGQf=[HcllcZDG shareHcllcZDG];
    NSLog(@"rsdkCode init success");
   }
    return wrapperCode;
}
@end
